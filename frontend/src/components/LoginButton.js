
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
  background-color: #D8BFD8;
  
  ${(props) =>
    props.signup &&
    `
    color: #fff;
    background: #BA55D3;
    margin-left: 35px;
    `}
  ${(props) =>
    props.signup2 &&
    `
    color: #fff;
    background: #BA55D3;
    `}
`;

export default function Button({ children, ...props }) {
  return <StyledButton {...props}>{children}</StyledButton>;
}