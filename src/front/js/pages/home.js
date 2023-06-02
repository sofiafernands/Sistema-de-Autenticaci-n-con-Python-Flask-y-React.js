import React, { useEffect, useContext }from "react";
import "../../styles/home.css";
import  { Card }  from "../component/card";
import { Context } from "../store/appContext";




//useContext se utiliza para acceder al objeto store y los actions de la aplicación que se han almacenado en el contexto Context, store y actions se ubican en flux
export const Home = () => {
	const { store, actions } = useContext (Context);

	

	return (
		<div className="container"> 
			{/* //characters */}
		<h1 className="display-4 py-1 fw-bolder text-center" style={{color:"#51c322",fontFamily:"fantasy"}}>Characters</h1>
		<div className="row d-flex flex-column wrapScroll mb-3  ">
		  <div className="cards d-flex  ">
			{store.characters.map((people, index) => { //mapeamos a characters dentro de cards
			  return (<div key={index} className="col-3"> <Card object={people} type="characters" id={index + 1} url={`/single/${people.id}`}/></div>)
			})}
		  </div>
		</div> 
		
	
			{/* Planets */}

			  <h1 className="display-4 py-1 fw-bolder text-center" style={{color:"black",fontFamily:"fantasy"}}>Planets</h1>
		<div className="row d-flex flex-column wrapScroll mb-3  ">
		  <div className="cards d-flex  ">
			{store.planets.map((planets, index) => { //mapeamos a planets dentro de cards
			  return (<div key={index} className="col-3"> <Card object={planets} type="planets" id={index + 2} url={`/single/${planets.id}`}/></div>)
			})}
		  </div>
		</div> 
		  
		  {/* vehicles */}

		  <h1 className="display-4 py-1 fw-bolder text-center" style={{color:"#51c322",fontFamily:"fantasy"}}>Vehicles</h1>
		<div className="row d-flex flex-column wrapScroll mb-3  " >
		  <div className="cards d-flex  " >
			{store.vehicles.map((vehicles, index) => { //mapeamos a planets dentro de cards
			  return (<div key={index} className="col-3"> <Card object={vehicles} type="vehicles" id={index + 4} url={`/single/${vehicles.id}`}/></div>)
			})}
		  </div>
		</div> 
			
	</div>
	
	);
};
 