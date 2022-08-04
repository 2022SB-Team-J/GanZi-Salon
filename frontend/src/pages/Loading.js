import { Link} from "react-router-dom";
import Spinner from 'react-bootstrap/Spinner';


const Loading = () => {
  
  return (
    <Link to="/AppliedStyleFinal" style={{ textDecoration: "none" }}>
    <div className="background-image-black"
    >
    
    <div className = "title-text-white-4"></div>
    <div style = {{textAlign : "center" , marginTop : "150px"}}>
    <Spinner animation="grow" variant="info" />
    <Spinner animation="grow" variant="info" />
    <Spinner animation="grow" variant="info" />
    <Spinner animation="grow" variant="info" />
    </div>
    <div className = "title-text-white-5">Now loading...</div>
    <div style = {{textAlign : "center"}}>
    <Spinner animation="grow" variant="info" />
    <Spinner animation="grow" variant="info" />
    <Spinner animation="grow" variant="info" />
    <Spinner animation="grow" variant="info" />
    </div>
    
    </div>
    </Link>
  );
}

export default Loading;
