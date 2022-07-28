import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/GenderButton";
import Slide from "../components/Slider";

function ChooseStyle() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black-3">Choose hair style or upload</div>
    <Button female> Female</Button>
    <Slide />
    <Button male> Male</Button>
    <Slide />
    <div style= {{textAlign : 'center'}}>
    {/*임시로 스타일/색깔 적용 완료 페이지로 이동시켰습니다.*/}
    <Link to="/AppliedStyleFinal" style={{ textDecoration: "none" }}>
        <Button  >Image upload</Button>
    </Link>
    </div>
    
    </div>
    
);
}

export default ChooseStyle;