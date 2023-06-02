import React,{ useEffect,useState,useContext } from "react";
import { BrowserRouter, Link, Route, Routes, useParams } from "react-router-dom";
//import "../../styles/demo.css";
import { Context } from "../store/appContext"; 



export const Card = (props) => {
  const { name } = useParams();
  const { store, actions }= useContext(Context);

  return (  // CHARACTERS-PLANETS-VEHICLES...ETC NOS SERVIRA PARA TODAS LAS VISTAS
   
      <div className="card" style={{ width: "300px",height:"100%", borderRadius:"20px" }}>
       <img src={`https://starwars-visualguide.com/assets/img/${props.type}/${props.id}.jpg`} 

         className="card-img-top"
         style={{ height: "100%", width: "100%",borderRadius:"20px" }}
         alt="Card image cap" />

       <div className="card-body" style={{fontSize:"12px",fontFamily:"fantasy"}}>
         <h5 className="card-title">{props.object.name} </h5>
         
 {/* link con la infomacion de cada personaje.*/}
        <Link className="btn btn-primary"  style={{background:"#575957"}} to={`/single/${props.type}/${props.id}`}>     
          Information
         </Link> 
{/* //BOTON DE FAVORIOTS */}
         <button
                  type="button"
                  style={{height:"37px", marginLeft:"40%"}}
                  className="btn btn-sm btn-outline-danger  "
                  onClick={() => {
                    actions.addToFavorites(props.object.name);
                  }}
                >
                   🖤  
                </button>
         
       </div>
     </div>
   )
  };

  
 


 
