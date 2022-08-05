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
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Popover from 'react-bootstrap/Popover';


const popover = (
  <Popover id="secondary">
    <Popover.Header as="h3">모델 선택 완료!</Popover.Header>
    <Popover.Body>
      결과를 확인하세요!
    </Popover.Body>
  </Popover>
);

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
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male01} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male02} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male03} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male04} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male05} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male06} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male07} alt = ""/>
          </OverlayTrigger>
          </div>
          <div>
          <OverlayTrigger trigger="click" placement="right" overlay={popover}>
          <img className="guideImg" src={male08} alt = ""/>
          </OverlayTrigger>
          </div>
        </Slider>
      </div>
    );
  }
}
