import React from "react";
import FemaleSlide from "../components/FemaleSlider";
import MaleSlide from "../components/MaleSlider";
import ModelUploader from "../components/ModelUploader";

function ChooseStyle() {
    
return (
    <div className="background-image-main">

    <div className = "title-text-black-3">Choose hair style or upload</div>
    <div style = {{marginLeft: '100px',  fontSize: '30px', fontFamily:'ariblk', paddingTop: '20px', color : '#9370db', fontWeight:'bold'}}>
    Female
    </div>
    <FemaleSlide />
    <div style = {{textAlign: 'center',  fontSize: '30px', fontFamily:'ariblk', paddingTop: '20px', color : 'Gray', fontWeight:'bold'}}>
    Please push to the side and select a picture.
    </div>
    <div style = {{marginLeft: '120px', fontSize: '30px', fontFamily:'ariblk', paddingTop: '20px', color : '#4682b4', fontWeight:'bold'}}>
    Male
     </div>
    <MaleSlide />
    <div style= {{textAlign : 'center'}}>
    {/*임시로 스타일/색깔 적용 완료 페이지로 이동시켰습니다.*/}
    
        <ModelUploader/>
    
    </div>
    
    </div>
    
);
}

export default ChooseStyle;
