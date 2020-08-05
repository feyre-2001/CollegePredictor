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
            # WORK ON SENDING FLASHES
            flash("You need to enter either a Rank or a Perentile")
            return render_template("public/index.html")

        if(rank==""):
            rank=-1;

        #TO PRINT AND ACCESS ALL THE DETAILS:
        # print(req)

        #TO GET A SPECIFIC FIELD AND USE ITS DATA AND I THINK YAHI USE KARNA HOGA
        print(percentile,rank,state,pwd,gender,category)
        return render_template("public/result.html")
    return render_template("public/index.html")
