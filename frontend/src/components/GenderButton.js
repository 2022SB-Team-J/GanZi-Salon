
import React from "react";
import styled from "styled-components";


    const StyledButton = styled.button`
    font-size: 23px;
    font-weight: 600;
    line-height: 49px;
    display: block;
    width: 360px;
    height: 70px;
    margin: 75px auto;
    cursor: pointer;
    text-align: center;
    color: black;
    border: none;
    border-radius: 50px;
    background-color: #E6E6FA;
    
    margin-top: 35px;

    ${(props) =>
    props.female &&
    `
    
    color: #fff;
    background: #FFC0CB;
    display: inline-block;
    width: 150px;
    height: 50px;

    margin-bottom: 10px;
    margin-top: 30px;

    margin-left: 30px;

    `
    }

    ${(props) =>
    props.male &&
    `
    
    color: #fff;
    background: #B0E0E6;
    display: inline-block;
    width: 150px;
    height: 50px;

    margin-bottom: 10px;
    margin-top: 30px;

    margin-left: 30px;


    `}
    `;

export default function Button({ children, ...props }) {
  return <StyledButton {...props}>{children}</StyledButton>;
}