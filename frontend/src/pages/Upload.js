import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/UploadButton";
import SelfieUploader from "../components/SelfieUploader";

function Upload() {
    
return (
    <div className="background-image-white">

    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    </div>
    <div className="selfie-text">Upload your selfie</div>
    <SelfieUploader/>

    <div style= {{textAlign : 'center'}}>
    <Link to="/ChooseStyle" style={{ textDecoration: "none" }}>
        <Button style >Change Style</Button>
    </Link>
    </div>

    </div>
    
);
}

export default Upload;
