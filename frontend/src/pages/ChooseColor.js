import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/PageButton";


function ChooseColor() {
    
return (
    <div className="background-image-white">

    <div className = "title-text-black">Choose hair color or upload</div>
    
    <div style={{display: 'flex' ,  justifyContent:'center'}}>
    {/* 스타일/컬러 적용할 모델 이미지 파일 4개 넣어주시면 됩니다.*/}
    <div className = "testimage-1"></div> 
    <div className = "testimage-2"></div>
    <div className = "testimage-3"></div>
    <div className = "testimage-4"></div>
    </div>

    <div style= {{textAlign : 'center'}}>
    <Link to="/History" style={{ textDecoration: "none" }}>
        <Button blueButton >Loading History</Button>
    </Link>
    {/*임시로 스타일/색깔 적용 완료 페이지로 이동시켰습니다.*/}
    <Link to="/AppliedColor" style={{ textDecoration: "none" }}>
        <Button redButton >Image upload</Button>
    </Link>
    </div>
    
    </div>
    
);
}

export default ChooseColor;