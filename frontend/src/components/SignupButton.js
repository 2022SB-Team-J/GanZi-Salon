import React from "react";
import styled from "styled-components";


const StyledButton = styled.button`
  font-size: 15px;
  font-weight: 700;
  line-height: 49px;
  display: block;
  width: 100px;
  height: 49px;
  margin: 0px;
  cursor: pointer;
  text-align: center;
  display: inline-block;
  color: #fff;
  border: none;
  border-radius: 25px;
  background-color: #D8BFD8;

  margin-left: 140px;


  ${(props) =>
    props.signup &&
    `
    color: #fff;
    background: #BA55D3;
    margin-left: 100px;

  `}
  ${(props) =>
    props.female &&
    `
    position: absolute; 
    color: #fff;
    background: #FF1493;
    
    `}
  ${(props) =>
    props.male &&
    `
    color: #fff;
    background: #00BFFF;
    position: absolute; 
    left:50%;
    margin-left:100px
    `}
  `;
  
  
  export default function Button({ children, ...props }) {
    return <StyledButton {...props}>{children}</StyledButton>;
  }
