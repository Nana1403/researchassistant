from flask import Flask, request, render_template, jsonify, request
import os
import asyncio
from dotenv import load_dotenv
from agent import main_agent
from fpdf import FPDF
from agents import Runner
from flask import send_file
from weasyprint import HTML
import bleach
from bleach.css_sanitizer import CSSSanitizer
import io
import markdown


load_dotenv()

main = Flask(__name__)

history = []

@main.route("/", methods=["GET", "POST"])
def mainpage():
   if request.method == "GET": 
       return render_template("mainpage.html")
   
   action = request.form.get("action")

   if action == "assi-page": 
      return render_template("assistantpage.html")

   return render_template("mainpage.html")

@main.route("/assistant", methods=["GET", "POST"])
def assistant():
   user_question = " "

   action = request.form.get("assistant")

   if action == "research":
      
      user_question = request.form.get("question", "")

      if not user_question:
          return render_template(
            "assistantpage.html",
            messages=history,
            user=user_question,
            error="Please enter a question."
        )

      history.append({"sender": "user", "text": user_question})

      result = asyncio.run(Runner.run(main_agent, user_question))
      
      assistant_markdown = result.final_output

      assistant_html = markdown.markdown( assistant_markdown, extensions=["extra"] )
      
      history.append({ "sender": "assistant", "text": assistant_html })
      
      return render_template("assistantpage.html", messages=history, user=user_question)
   return render_template("assistantpage.html", messages=history, user=user_question) 

@main.route("/save-pdf", methods=["POST"])
def save_pdf():
    content = request.form.get("content", "")

    css_sanitizer = CSSSanitizer(
    allowed_css_properties=[
        "color",
        "background-color",
        "font-size",
        "font-family",
        "font-weight",
        "font-style",
        "text-decoration",
        "text-align"
      ]
    )

    clean_content = bleach.clean(
        content,
        tags=[
            "p", "br", "strong", "b", "em", "i", "u",
            "h1", "h2", "h3",
            "ul", "ol", "li",
            "span"
        ],
        attributes={
             "span": ["style"],
             "p": ["style"],
             "h1": ["style"],
             "h2": ["style"],
             "h3": ["style"]
          }, 
        css_sanitizer=css_sanitizer
        
        )

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          font-family: Arial, sans-serif;
          font-size: 14px;
          color: black; 
          line-height: 1.5;
          padding: 30px;
        }}
      </style>
    </head>
    <body>
      {clean_content}
    </body>
    </html>
    """

    pdf_file = io.BytesIO()
    HTML(string=html).write_pdf(pdf_file)
    pdf_file.seek(0)

    return send_file(pdf_file, as_attachment=True, download_name="note.pdf",  mimetype="application/pdf" )




if __name__ == '__main__':
   main.run(debug=True)