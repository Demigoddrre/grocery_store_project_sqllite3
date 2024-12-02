from flask import Flask, render_template

app = Flask(__name__)

@app.route("/view_report/<embed_url>")
def view_report(embed_url):
    return render_template("report_viewer.html", embed_url=embed_url)

if __name__ == "__main__":
    app.run(debug=True)
