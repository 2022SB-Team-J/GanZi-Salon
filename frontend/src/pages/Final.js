
import React from "react";
import { Link } from 'react-router-dom';
import Button from "../components/FinalButton";

function Final() {
return (
  <div className="background-image2">
  <div style={{
  textAlign:'center',
  border : '1px',
  height : '250px',
  display : 'flex',
  justifyContent : 'center',
  alignItems : 'center',
  fontSize: '100px',
  fontFamily: 'ganzisalon_font'
  }}>
  Beautiful Hair!
  </div>

  <div style= {{textAlign : 'center',
  marginTop: '450'}}>
  <Link to="/History">
    <Button> Done&Save</Button>
  </Link>

  <Link to="/Title">
    <Button share> Share</Button>
  </Link>
</div>
</div>
);
}

export default Final;
