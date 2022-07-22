

import React from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";
import Button from "../components/LoginButton";
import Input from "../components/IdPassword";

//백엔드와 프론트 통신 객체
import axios from "axios"


const Container = styled.div`
  margin-top: 100px;
  padding: 20px;
  text-align: center;
`;

function SignUp() {

//    회원가입 버튼 클릭 시 동작
//    참고링크 >> https://velog.io/@dev_bomdong/React-회원가입-기능-구현하기
    const handleSubmit = () => {
        e.preventDefault();
        try {
            fetch('API주소', {
                method: 'POST',
                body: JSON.stringify({
                    username: this.state.username,
                    id: this.state.id,
                    password: this.state.password,
                    gender: 'w'
                }),
            })
                .then(response => response.json());
        } catch (err) {
            alert('회원가입 실패입니다.');
        }
    };


return (
    
    <Container className="background-image-black" >
      
    <form style = {{marginTop : '250px', marginBottom: '30px'}}
            onSubmit={handleSubmit}>
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
      </form>
    </Container>
  );
}

export default Login;