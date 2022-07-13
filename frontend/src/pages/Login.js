
import React from "react";
import styled from "styled-components";

const Container = styled.div`
  margin-top: 100px;
  padding: 20px;
  text-align: center;
`;

const Input = styled.input`
  position: relative;
  overflow: hidden;
  width: 20%;
  height: 40px;
  margin: 0 0 8px;
  padding: 5px 39px 5px 11px;
  border: solid 1px #dadada;
  background: #fff;
  box-sizing: border-box;
`;

const Button = styled.div`
  font-size: 18px;
  font-weight: 700;
  line-height: 49px;
  display: block;
  width: 100px;
  height: 49px;
  margin: 16px 0 7px;
  cursor: pointer;
  text-align: center;
  display: inline-block;
  color: #fff;
  border: none;
  border-radius: 13px;
  background-color: #03c75a;
  

  
  ${({ disabled }) =>
    disabled &&
    `
    background-color: #efefef;
  `}
`;
//아디 비번 값 받기
//값없으면 disabled
function LoginForm() {
return (
    
    <Container className="background-image" >
    <div style = {{marginTop : '300px'}}>
    <div>
    <Input id="id" name="id" placeholder="아이디를 입력해주세요" />
    </div>
    <Input
        id="password"
        name="password"
        type="password"
        placeholder="비밀번호를 입력해주세요"
      />
      
      <div style = {{textAlign : 'center'}}>
      <Button>로그인</Button>
      <Button style = {{marginLeft : '100px'}}>회원가입</Button>
      </div>
      </div>
    </Container>
  );
}

export default LoginForm;