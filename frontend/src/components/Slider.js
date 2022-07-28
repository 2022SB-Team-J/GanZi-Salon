import React, { Component } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import modelImg01 from "../images/testimage01.png";
import modelImg02 from "../images/testimage02.png";
import modelImg03 from "../images/testimage03.png";
import modelImg04 from "../images/testimage04.png";
import modelImg05 from "../images/testimage05.png";
import modelImg06 from "../images/testimage06.png";
import modelImg07 from "../images/testimage07.png";
import modelImg08 from "../images/testimage08.png";


export default class SwipeToSlide extends Component {
  render() {
    const settings = {
      className: "center",
      infinite: true,
      centerPadding: "60px",
      slidesToShow: 5,
      swipeToSlide: true,
      afterChange: function(index) {
        console.log(
          `Slider Changed to: ${index + 1}, background: #222; color: #bada55`
        );
      }
    };
    return (
      <div>
        
        <Slider {...settings}>
          <div>
          <img className="guideImg" src={modelImg01} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg02} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg03} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg04} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg05} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg06} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg07} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={modelImg08} alt = ""/>
          </div>
        </Slider>
      </div>
    );
  }
}