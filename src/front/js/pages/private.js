import React, {useContext, useEffect, useState} from "react";
import { Context } from "../store/appContext"






export const Private = () => {
    const {store,actions} = useContext(Context)
    useEffect(() => {
        actions.private()
    },
   [])
   return (
    <>
    {store.auth && store.auth? "private":"public"}
    </>
   )

}
