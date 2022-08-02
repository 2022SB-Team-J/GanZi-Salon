
import React from "react";
import styled from "styled-components";


const StyledButton = styled.button`
  font-size: 15px;
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
  border-radius: 25px;
  background-color: #BA55D3;
  
  ${(props) =>
    props.signup &&
    `
    position: absolute; 
    color: #fff;
    background: #D8BFD8;
    
    `}
  ${(props) =>
    props.signin &&
    `
    color: #fff;
    background: #BA55D3;
    position: absolute; 
    left:50%;
    margin-left:100px
    `}
    ${(props) =>
      props.signup2 &&
      `
      color: #fff;
      background: #D8BFD8;
      position: absolute; 
      left:50%;
      margin-left:-57px
      
      
      
      `}
      ${(props) =>
        props.style &&
        `
        
        color: #fff;
        background: #B0E0E6;
        display: inline-block;
        width: 200px;
        margin-left: 0px;
        `
        }
`;

export default function Button({ children, ...props }) {
  return <StyledButton {...props}>{children}</StyledButton>;
}