import React from "react";
import Button from "../components/HistoryButton";
import { Link } from "react-router-dom";
import result1 from "../images/result/1_result.jpg";
import result2 from "../images/result/2_result.jpg";
import result3  from "../images/result/3_result.jpg";
import result4  from "../images/result/4_result.jpg";

function History() {
    return(

<div className = "background-image-main" >
    
<div className = "title-text-black"  >Your History</div>
<div style = {{marginLeft: '1280px', fontSize: '30px', color:'#941494' , fontWeight:"800"}}>NEW!</div>
<div style = {{marginTop: '30px'}}>
<div style= {{float: 'left', width: '25%'}}>
<img className="historyImage" src={result1} alt = ""/>
</div>
<div style= {{float: 'left', width: '25%'}}>
<img className="historyImage" src={result2} alt = ""/>
</div>
<div style= {{float: 'left', width: '25%'}}>
<img className="historyImage" src={result3} alt = ""/>
</div>
<div style= {{float: 'left', width: '25%'}}>
<img className="historyImage" src={result4} alt = ""/>
</div>
</div>
<Link to="/Title" style={{ textDecoration: "none" }}>
<div style = {{marginTop: '300px'}}>
<Button>Home</Button>
</div>
</Link>
</div>



);
}
export default History;