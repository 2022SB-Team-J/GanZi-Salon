import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/TitleButton";


function Title() {
    
return (
    <div className="background-image-white">
    <div className = "title-text-black">GanZi Salon</div>

    
    <Link to="/History" style={{ textDecoration: "none" }}>
    <Button > History</Button>
    
    </Link>
    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    

    </div>
    
    <div style= {{textAlign : 'center'}}>
    <Link to="/Upload" style={{ textDecoration: "none" }}>

        <Button style >Upload Selfie</Button>

    </Link>
    </div>
    </div>
    
);
}

export default Title;