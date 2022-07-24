

import React  from "react";
// import styled from "styled-components";
import Button from "../components/LoginButton";
import Input from "../components/IdPassword";
import axios from "axios";
import {toast, ToastContainer} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import {Formik, ErrorMessage} from "formik";
import * as Yup from "yup";
import { Link } from "react-router-dom";
import "../css/signUp.scss";

const SignUp = () => {

    const validationSchema = Yup.object().shape({
    username: Yup.string()
        .min(2, "아이디는 최소 2글자 이상입니다!")
        .max(10, "아이디는 최대 10글자입니다!")
        ,
    email: Yup.string()
        .email("올바른 이메일 형식이 아닙니다!")
        ,

    password: Yup.string()
        .min(4, "비밀번호는 최소 4자리 이상입니다")
        .max(16, "비밀번호는 최대 16자리입니다!")
        ,
    password2: Yup.string()
        .oneOf([Yup.ref("password"), null], "비밀번호가 일치하지 않습니다!")
        ,
    });
    const submit = async (values) => {
    const {email, username, password} = values;
    try {
        await axios.post("/api/auth/signup", {
        email,
        username,
        password,
        });
        toast.success(<h3>회원가입이 완료되었습니다.<br/>로그인 하세요😎</h3>, {
        position: "top-center",
        autoClose: 2000
        });
        setTimeout(()=> {
            <Link to="/Title"/>
        }, 2000);

    } catch (e) {
        // 서버에서 받은 에러 메시지 출력
        toast.error(e.response.data.message + "😭", {
        position: "top-center",
        });
    }
};
  
    return (
      <Formik
        initialValues={{
        username: "",
        email: "",
        password: "",
        password2: "",
        }}
        validationSchema={validationSchema}
        onSubmit={submit}
        validateOnMount={true}
      >
        {({values, handleSubmit, handleChange, errors}) => (
        <div className="background-image-black">
            <div className="signup-wrapper">
            <ToastContainer />

            <div style = {{marginTop : '100px', marginBottom: '30px'}}>
            <div className = "title-text-white"  >GANZI SALON </div>
            <div className = "title-text-white-3"  >SIGN UP </div>
            <form onSubmit={handleSubmit} autoComplete="off">
            <div className="input-forms">
                <div className="input-forms-item">
                <Input
                    value={values.username}
                    name="username"
                    variant="outlined"
                    onChange={handleChange}
                    placeholder="name"
                />
                <div className="error-message">
                    {errors.username}
                </div>
                
                <div className="input-forms-item">
                <Input
                    value={values.email}
                    name="email"
                    variant="outlined"
                    placeholder="email"
                    onChange={handleChange}
                />
                <div>
                    {errors.email}
                </div>
                </div>
                </div>

                <div className="input-forms-item">
                <Input
                    value={values.password}
                    name="password"
                    variant="outlined"
                    type="password"
                    placeholder="password"
                    onChange={handleChange}
                />
                <div className="error-message">
                    {errors.password}
                </div>
                </div>

                <div className="input-forms-item">
                <Input
                    value={values.password2}
                    name="password2"
                    variant="outlined"
                    type="password"
                    placeholder="password check"
                    onChange={handleChange}
                />
                <div className="error-message">
                    {errors.password2}
                </div>
                </div>

                <Button signup2
                variant="contained"
                fullWidth
                type="submit"
                >
                회원가입
                </Button>
            </div>
            </form>
        </div>
        </div>
        </div>
        )}
    </Formik>
    );
};

export default SignUp;

// const Container = styled.div`
// margin-top: 100px;
// padding: 20px;
// text-align: center;
// `;


//     function SignUp() {

// return (
    
//     <Container className="background-image-black" >
    
//     <form style = {{marginTop : '250px', marginBottom: '30px'}}>
//     <div className = "title-text-white"  >GANZI SALON</div>
//         <div>
//         <Input
//         id="name"
//         name="name"
//         type="name"
//         placeholder="NAME"
//         />
//         </div>
//         <div>
//         <Input
//         id="gender"
//         name="gender"
//         type="gender"
//         placeholder="GENDER"
//         />
//         </div>
//         <div>
//         <Input
//         id="password"
//         name="password"
//         type="password"
//         placeholder="PASSWORD"
//         />
//         </div>
//         <div>
//         <Input
//         id="password"
//         name="password"
//         type="password"
//         placeholder="PASSWORD CONFIRM"
//         />
//         </div>
//     <div style = {{textAlign : 'center'}}>
//       {/* 임시로 Title 페이지로 이동하게 세팅 */}
    
    
//         <Button>Create account</Button>
    
//     </div>
//     </form>
//     </Container>
    
//   );
// }

// export default SignUp;