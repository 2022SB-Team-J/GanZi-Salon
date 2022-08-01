import React from "react";
import FemaleSlide from "../components/FemaleSlider";
import MaleSlide from "../components/MaleSlider";
import ModelUploader from "../components/ModelUploader";
import Button from "../components/GenderButton";

function ChooseStyle() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black-3">Choose hair style or upload</div>
    <Button female> Female</Button>
    <FemaleSlide />
    <Button male> Male</Button>
    <MaleSlide />
    <div style= {{textAlign : 'center'}}>
    {/*임시로 스타일/색깔 적용 완료 페이지로 이동시켰습니다.*/}
    
        <ModelUploader/>
    
    </div>
    
    </div>
    
);
}

export default ChooseStyle;
