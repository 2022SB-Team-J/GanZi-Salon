import React from "react";
import { Link } from "react-router-dom";
import Button from "../../components/PageButton";


function AppliedColor() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black">Applied color</div>
    
    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    <div className = "testimage-1"></div> 
    </div>

    <div style= {{textAlign : 'center'}}>
    <Link to="/Title" style={{ textDecoration: "none" }}>
        <Button blueButton >Done & Save</Button>
    </Link>
    <Link to="/AppliedStyleFinal" style={{ textDecoration: "none" }}>
        <Button redButton >Finish</Button>
    </Link>
    </div>
    
    </div>
    
);
}

export default AppliedColor;