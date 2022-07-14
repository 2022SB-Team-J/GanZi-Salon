import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/TitleButton";


function Title() {
    
return (
    <div className="background-image-white">
    <div className = "title-text-black">GanZi Salon</div>

    
    <Link to="/" style={{ textDecoration: "none" }}>
    <Button > History</Button>
    
    </Link>
    

    <div style= {{textAlign : 'center'}}>
    <Link to="/ChangeStyle" style={{ textDecoration: "none" }}>

        <Button style >Change Style</Button>

    </Link>
    
    
    <Link to="/ChangeColor" style={{ textDecoration: "none" }}>

        <Button color >Change Color</Button>

    </Link>
    </div>
    </div>
    
);
}

export default Title;