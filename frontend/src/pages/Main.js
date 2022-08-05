import { Link} from "react-router-dom";



const Main = () => {
  
  return (
    <Link to="/Login" style={{ textDecoration: "none" }}>
    <div className="background-image-black"
    >
    
    <div className = "title-text-white-6">Welcome</div>
    <div style = {{textAlign : "center" , marginTop : "100px"}}>
    </div>
    <div className = "title-text-white-5">GanZI Salon</div>
    <div style = {{textAlign : "center"}}>
    </div>
    
    </div>
    </Link>
  );
}

export default Main;
