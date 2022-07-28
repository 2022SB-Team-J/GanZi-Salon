import React, { Component } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import modelImg01 from "../images/testimage01.png";
import modelImg02 from "../images/testimage02.png";
import modelImg03 from "../images/testimage03.png";
import modelImg04 from "../images/testimage04.png";

export default class LazyLoad extends Component {
    render() {
      const settings = {
        dots: true,
        lazyLoad: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        initialSlide: 2
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
        </Slider>
      </div>
    );
  }
}