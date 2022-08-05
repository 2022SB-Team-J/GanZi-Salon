import React from "react";
import Button from "../components/HistoryButton";
import { Link } from "react-router-dom";

import result4  from "../images/result/firstResult.jpg";

function History() {
    return(

<div className = "background-image-main" >
    
<div className = "title-text-black"  >Your History</div>
<div style = {{marginLeft: '715px', fontSize: '30px', color:'#941494' , fontWeight:"800"}}>NEW!</div>
<div style = {{marginTop: '30px'}}>

<div style= {{float: 'left', width: '100%'}}>
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