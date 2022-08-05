import React, { Component } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import male01 from "../images/model/male01.jpeg";
import male02 from "../images/model/male02.jpeg";
import male03 from "../images/model/male03.jpeg";
import male04 from "../images/model/male04.jpeg";
import male05 from "../images/model/male05.jpeg";
import male06 from "../images/model/male06.jpeg";
import male07 from "../images/model/male07.jpeg";
import male08 from "../images/model/male08.jpeg";





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
          
          <img className="guideImg" src={male01} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male02} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male03} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male04} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male05} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male06} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male07} alt = ""/>
          
          </div>
          <div>
          
          <img className="guideImg" src={male08} alt = ""/>
          
          </div>
        </Slider>
      </div>
    );
  }
}
