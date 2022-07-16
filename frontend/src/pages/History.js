import React from "react";
import Button from "../components/HistoryButton";
import { Link } from "react-router-dom";
function History() {
    return(
<div>
<div className = "background-image-white" >


<div className = "title-text-black"  >YOUR HISTORY</div>
<Link to="/Title" style={{ textDecoration: "none" }}>
<Button>Home</Button>
</Link>
</div>


</div>

);
}
export default History;