import React, { Component } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import Female01 from "../images/model/Female01.jpeg";
import Female02 from "../images/model/Female02.jpeg";
import Female03 from "../images/model/Female03.jpeg";
import Female04 from "../images/model/Female04.jpeg";
import Female05 from "../images/model/Female05.png";
import Female06 from "../images/model/Female06.jpeg";
import Female07 from "../images/model/Female07.jpeg";
import Female08 from "../images/model/Female08.jpeg";


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
          <div >
          <img className="guideImg" src={Female01} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female02} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female03} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female04} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female05} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female06} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female07} alt = ""/>
          </div>
          <div>
          <img className="guideImg" src={Female08} alt = ""/>
          </div>
        </Slider>
      </div>
    );
  }
}