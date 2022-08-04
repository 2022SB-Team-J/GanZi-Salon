import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/PageButton";


function AppliedStyleFinal() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black">Beautiful Hair!</div>
    
    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    <div className = "resultImage"></div> 
    </div>

    <div style= {{textAlign : 'center'}}>
    <Link to="/History" style={{ textDecoration: "none" }}>
        <Button blueButton >Done & Save</Button>
    </Link>
    {/* 임시로 Title 페이지로 이동하게 세팅 */}
    </div>
    
    </div>
    
);
}

export default AppliedStyleFinal;
