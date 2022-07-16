import React from "react";
import styled from "styled-components";

const StyledInput = styled.input`
  position: relative;
  overflow: hidden;
  width: 275px;
  height: 50px;
  margin: 0 0 8px;
  padding: 5px 39px 5px 11px;
  border: solid 1px #dadada;
  background: #D3D3D3;
  box-sizing: border-box;
  border-radius: 15px;
`;

export default function Input({ children, ...props }) {
    return <StyledInput {...props}>{children}</StyledInput>;
  }