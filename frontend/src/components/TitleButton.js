import React from "react";
import styled from "styled-components";


    const StyledButton = styled.button`
    font-size: 25px;
    font-weight: 700;
    line-height: 49px;
    width: 160px;
    height: 80px;
    margin-top: 37px;
    margin-left: 150px;
    margin: 100px auto;
    display: block;
    cursor: pointer;
    color: black;
    border: none;
    border-radius: 50px;
    background-color: #E6E6FA;
    
    ${(props) =>
    props.style &&
    `
    
    color: #fff;
    background: #B0E0E6;
    display: inline-block;
    width: 250px;
    margin-left: 0px;
    margin: 40px auto;
    `
    
    }

    ${(props) =>
    props.color &&
    `
    color: #fff;
    background: #FFC0CB;
    margin-left: 35px;    
    display: inline-block;
    width: 250px;
    `}
    `;

export default function Button({ children, ...props }) {
  return <StyledButton {...props}>{children}</StyledButton>;
}