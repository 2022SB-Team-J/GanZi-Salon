import React from "react";

import SelfieUploader from "../components/SelfieUploader";

function Upload() {
    
return (
    <div className="background-image-white">

    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    </div>
    <div className="selfie-text">Upload your selfie</div>
    <SelfieUploader/>

    <div style= {{textAlign : 'center'}}>

    </div>
    </div>
    
);
}

export default Upload;
