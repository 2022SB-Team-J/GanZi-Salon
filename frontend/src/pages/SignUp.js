

import React from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";
import Button from "../components/LoginButton";
import Input from "../components/IdPassword";

const Container = styled.div`
  margin-top: 100px;
  padding: 20px;
  text-align: center;
`;

function Login() {
return (
    
    <Container className="background-image-black" >
      
    <div style = {{marginTop : '250px', marginBottom: '30px'}}>
    <div className = "title-text-white"  >GANZI SALON</div>

    <div>
    <Input 
    id="id" 
    name="id" 
    placeholder="ID" 
    />
    </div>
    <div>
    <Input
    id="password"
    name="password"
    type="password"
    placeholder="PASSWORD"
    />
    </div>
    <div>
    <Input
    id="username"
    name="username"
    type="username"
    placeholder="NAME"
    />
    </div>
      <div style = {{textAlign : 'center'}}>
      {/* 임시로 Title 페이지로 이동하게 세팅 */}
      
      <Link to="/" style={{ textDecoration: "none" }}>
      <Button signup2>Sign up</Button>
      </Link> 
      </div>
      </div>
    </Container>
  );
}

export default Login;