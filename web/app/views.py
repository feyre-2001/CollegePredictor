from app import app

from flask import render_template, request, redirect, flash

@app.route("/", methods=["GET","POST"])
def index():
    if(request.method=="POST"):
        req=request.form

        percentile=req["percentile"]
        rank=req["rank"]
        state=req["state"]
        pwd=req["pwd"]
        gender=req["gender"]
        category=req["category"]


        if(percentile=="" and rank==""):
            flash("Please enter either your Rank or your Percentile",'error')
            return redirect(request.url)


        if(rank==""):
            rank=-1;

        if(percentile==""):
            percentile=-1;



        #TO GET A SPECIFIC FIELD AND USE ITS DATA AND I THINK YAHI USE KARNA HOGA
        print(percentile,rank,state,pwd,gender,category)
        return render_template("public/result.html",rank=rank, category=category)
    return render_template("public/index.html")
