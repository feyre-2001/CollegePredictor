import secrets;
from app import app;
from .rvp import pvr;
from .algo import finalList;

from flask import render_template, request, redirect, flash

@app.route("/", methods=["GET","POST"])
def index():

    secret_key=secrets.token_hex(16)
    app.config["SECRET_KEY"] = secret_key

    if(request.method == "POST"):
        req = request.form

        percentile = req["percentile"]
        rank = req["rank"]
        state = req["state"]
        pwd = req["pwd"]
        gender = req["gender"]
        category = req["category"]
        sortby = str(req["sortby"])

        if(percentile == "" and rank == ""):
            flash("Please enter either your Rank or your Percentile",'error')
            return redirect(request.url)

        if(rank == ""):
            ranks = pvr(float(percentile),pwd,category);
            ranks = int(ranks);

            if(ranks <= 0):
                ranks = 2;
            result = finalList(ranks,float(percentile),category,state,gender,pwd,sortby);

        if(rank):
            result = finalList(int(rank),percentile,category,state,gender,pwd,sortby);
            ranks = rank;

        return render_template("public/result.html",ranks=ranks,category=category,tables=[result.to_html(classes='data')], titles=result.columns.values)

    return render_template("public/index.html")
