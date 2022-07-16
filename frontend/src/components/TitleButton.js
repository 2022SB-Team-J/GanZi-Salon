
import React from "react";
import styled from "styled-components";


    const StyledButton = styled.button`
    font-size: 25px;
    font-weight: 700;
    line-height: 49px;
    display: block;
    width: 360px;
    height: 100px;
    margin: 75px auto;
    cursor: pointer;
    text-align: center;
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