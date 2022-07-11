
import React from "react";
import { Link } from "react-router-dom";

function Title() {
return (
    <div >
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
    
    </div>
    
);
}

export default Title;