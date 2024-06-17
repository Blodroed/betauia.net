from flask import Blueprint, render_template

from .utils import read_markdown

betadev_bp = Blueprint("betadev", __name__)

@betadev_bp.route("/")
def betadev():
    content = read_markdown("betadev")
    return render_template("blank.html", title="BetaDEV", content=content)

@betadev_bp.route("/wiki")
def wiki():
    content = read_markdown("betadev/wiki")
    return render_template("blank.html", title="Dev wiki", content=content)
