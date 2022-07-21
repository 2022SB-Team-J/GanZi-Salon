import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/PageButton";


function AppliedStyleFinal() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black">Beautiful Hair!</div>
    
    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    <div className = "testimage-1"></div> 
    </div>

    <div style= {{textAlign : 'center'}}>
    <Link to="/Title" style={{ textDecoration: "none" }}>
        <Button blueButton >Done & Save</Button>
    </Link>
    {/* 임시로 Title 페이지로 이동하게 세팅 */}
    <Link to="/Title" style={{ textDecoration: "none" }}>
        <Button redButton >Share</Button>
    </Link>
    </div>
    
    </div>
    
);
}

export default AppliedStyleFinal;
