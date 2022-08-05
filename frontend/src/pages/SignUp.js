import React  from "react";
// import styled from "styled-components";
import Button from "../components/SignupButton";
import Input from "../components/IdPassword";
import axios from "axios";
import {toast, ToastContainer} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import {Formik} from "formik";
import * as Yup from "yup";
import { Link } from "react-router-dom";
import "../css/signUp.css";

const SignUp = () => {

    const validationSchema = Yup.object().shape({
    id: Yup.string()
        
        ,
    gender: Yup.string()
        
        ,

    password: Yup.string()
        ,
    password2: Yup.string()
        ,
    });
    const submit = async (values) => {
    const {id, gender, password} = values;
    try {
        await axios.post("/api/auth/join", {
        id,
        gender,
        password,
        });
        toast.success(<h3>회원가입이 완료되었습니다.<br/>로그인 하세요😎</h3>, {
        position: "top-center",
        autoClose: 2000
        });
        setTimeout(()=> {
            <Link to="/Login"/>
        }, 2000);

    } catch (e) {
        // 서버에서 받은 에러 메시지 출력
        toast.success("회원가입 완료", {
        position: "top-center",
        });
    }
};
  
    return (
      <Formik
        initialValues={{
        id: "",
        gender: "",
        password: "",
        password2: "",
        }}
        validationSchema={validationSchema}
        onSubmit={submit}
        validateOnMount={true}
      >
        {({values, handleSubmit, handleChange, errors}) => (
        <div className="background-image-black">
            <Button female style = {{bottom: '408px' , right: '870px'}}>female</Button>
                <Button male style = {{bottom: '408px'}}>male</Button>
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
                    name="name"
                    variant="outlined"
                    onChange={handleChange}
                    placeholder="name"
                />
                <div className="error-message">
                    {errors.username}
                </div>
                </div>
                <div className="input-forms-item">
                <Input
                    value={values.username}
                    name="id"
                    variant="outlined"
                    onChange={handleChange}
                    placeholder="id"
                />
                <div className="error-message">
                    {errors.username}
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
                    

    
                <Button signin
                margin-left= '150px'
                variant='contained'
                fullWidth
                type='submit'
                width='fit-content'
                margin='auto'
                
                
                >
                Sign up
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
