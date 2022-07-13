
import React from "react";
import { Link } from "react-router-dom";

function Title() {
return (
    <div className="background-image">
    <div >GanZi Salon</div>

    <Link to="/ChooseStyle" style={{ textDecoration: "none" }}>
    
        <div> Change style</div>
    
    </Link> 


    <Link to="/ChangeColor" style={{ textDecoration: "none" }}>

        <div >change color</div>

    </Link>
    
    <Link to="/History" style={{ textDecoration: "none" }}>

        <div  className="title">History</div>

    </Link>
    
    <Link to="/Login" style={{ textDecoration: "none" }}>

        <h1  >Go Login Page</h1>

    </Link>
    </div>
    
);
}

export default Title;