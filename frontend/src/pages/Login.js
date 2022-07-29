import React  from "react";
import axios from "axios";
import {toast, ToastContainer} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import {Formik, ErrorMessage} from "formik";
import * as Yup from "yup";
import Button from "../components/LoginButton";
import Input from "../components/IdPassword";
import { Link } from "react-router-dom";
import "../css/signUp.css";
import {useDispatch} from "react-redux";
import {setToken} from "../redux/reducers/AuthReducer";

<<<<<<< HEAD
const Container = styled.div`
  padding: 20px;
  text-align: center;
`;

function Login() {
return (
    
    <Container className="background-image-black" >
=======
const Login = () => {
  const dispatch = useDispatch();
  const validationSchema = Yup.object().shape({
    id: Yup.string()
      ,
    password: Yup.string()
>>>>>>> feature/join
      
  });
  const submit = async (values) => {
    const {id, password} = values;
    try {
      const {data} = await axios.post("/api/auth/login", {
        id,
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
        id: "",
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
                  value={values.id}
                  name="id"
                  variant="outlined"
                  placeholder="id"
                  onChange={handleChange}
                />
                <div className="error-message">
                  <ErrorMessage name="id"/>
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
              <Link to="/signup">
              <Button signup>
                회원가입
              </Button>
              </Link>
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