import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/PageButton";
import Slide from "../components/Slider";

function ChooseStyle() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black-2">Choose hair style or upload</div>

    <Slide />

    <Slide />
    <div style= {{textAlign : 'center'}}>
    <Link to="/History" style={{ textDecoration: "none" }}>
        <Button blueButton >Loading history</Button>
    </Link>
    {/*임시로 스타일/색깔 적용 완료 페이지로 이동시켰습니다.*/}
    <Link to="/AppliedStyleFinal" style={{ textDecoration: "none" }}>
        <Button redButton >Image upload</Button>
    </Link>
    </div>
    
    </div>
    
);
}

export default ChooseStyle;