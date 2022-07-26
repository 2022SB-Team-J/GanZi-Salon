import React  from "react";
import axios from "axios";
import {toast, ToastContainer} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import {Formik, ErrorMessage} from "formik";
import * as Yup from "yup";
import Button from "../components/LoginButton";
import Input from "../components/IdPassword";
import { Link } from "react-router-dom";
// SignUp 컴포넌트 scss 이용
import "../css/signUp.css";
import {useDispatch} from "react-redux";
import {setToken} from "../redux/reducers/AuthReducer";

const Login = () => {
  const dispatch = useDispatch();
  const validationSchema = Yup.object().shape({
    email: Yup.string()
      .email("올바른 이메일 형식이 아닙니다!")
      .required("이메일을 입력하세요!"),
    password: Yup.string()
      .required("패스워드를 입력하세요!")
  });
  const submit = async (values) => {
    const {email, password} = values;
    try {
      const {data} = await axios.post("/api/auth/signin", {
        email,
        password,
      });
      dispatch(setToken(data.jwt));
      toast.success(<h3>로그인 성공😎</h3>, {
        position: "top-center",
        autoClose: 2000,
      });
      setTimeout(() => {
        <Link to="/Title" />
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
        email: "",
        password: "",
      }}
      validationSchema={validationSchema}
      onSubmit={submit}
    >
      {({values, handleSubmit, handleChange}) => (
        <div className="background-image-black">
        <div className="signup-wrapper">
          <ToastContainer/>
          <div style = {{marginTop : '100px', marginBottom: '30px'}}>
            <div className = "title-text-white"  >GANZI SALON </div>
            <div className = "title-text-white-3"  >LOGIN </div>
          <form onSubmit={handleSubmit} autoComplete="off">
            <div className="input-forms">
              <div className="input-forms-item">
                
                <Input
                  value={values.email}
                  name="email"
                  variant="outlined"
                  onChange={handleChange}
                />
                <div className="error-message">
                  <ErrorMessage name="email"/>
                </div>
              </div>
              <div className="input-forms-item">
                
                <Input
                  value={values.password}
                  name="password"
                  variant="outlined"
                  type="password"
                  onChange={handleChange}
                />
                <div className="error-message">
                  <ErrorMessage name="password"/>
                </div>
              </div>
              <Button signin
                color="primary"
                variant="contained"
                fullWidth
                type="submit"
              >
                로그인
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

export default Login;
// import React from "react";
// import styled from "styled-components";
// import { Link } from "react-router-dom";
// import Button from "../components/LoginButton";
// import Input from "../components/IdPassword";

// const Container = styled.div`
//   margin-top: 100px;
//   padding: 20px;
//   text-align: center;
// `;

// function Login() {
// return (
//   <div className = "background-image-black">
//     <Container  >
    
//     <div style = {{marginTop : '250px', marginBottom: '30px'}}>
//     <div className = "title-text-white-2"  >GANZI SALON</div>
//     <div>
//         <Input 
//         id="id"
//         name="id" 
//         placeholder="ID" 
//         />
//     </div>
//         <Input
//         id="password"
//         name="password"
//         type="password"
//         placeholder="PASSWORD"
//         />
        
//       <div style = {{textAlign : 'center'}}>
//       {/* 임시로 Title 페이지로 이동하게 세팅 */}
//       <Link to="/SignUp" style={{ textDecoration: "none" }}>
//       <Button>Sign up</Button>
//       </Link> 
//       <Link to="/Title" style={{ textDecoration: "none" }}>
//       <Button signup>Sign in</Button>
//       </Link> 
      
//       </div>
//       </div>
      
//     </Container>
//     </div>
//   );
// }

// export default Login;