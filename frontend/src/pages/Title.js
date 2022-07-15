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
    {/* 스타일/컬러 적용할 모델 이미지 파일 4개 넣어주시면 됩니다.*/}
    <div className = "title-test-image"></div> 
    </div>
    <div className="selfie-text">Upload your selfie</div>
    <div style= {{textAlign : 'center'}}>
    <Link to="/ChooseStyle" style={{ textDecoration: "none" }}>

        <Button style >Change Style</Button>

    </Link>
    
    
    <Link to="/ChooseColor" style={{ textDecoration: "none" }}>

        <Button color >Change Color</Button>

    </Link>
    </div>
    </div>
    
);
}

export default Title;