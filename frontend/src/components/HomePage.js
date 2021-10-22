import React, { Component } from 'react'
import CreateRoomPage from "./CreateRoomPage"
import RoomJoinPage from "./RoomJoinPage"
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom"

export default class HomePage extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return <Router>
            <Switch>
                <Route exact path='/'><p>This is the home page</p></Route>    // exact!!!!!!!!!! (иначе будут одинаковые адреса)
                <Route path='/join' component={RoomJoinPage} />
                <Route path='/create-room' component={CreateRoomPage} />
               </Switch>
        </Router>
    }
}