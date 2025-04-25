import { BrowserRouter, Routes, Route } from "react-router"
import { Login } from '../pages/forms/Login'
import { Initial } from '../pages/Initial'
import { TeacherRegister } from "../pages/forms/TeacherRegister"
import { EnviromentRegister } from '../pages/forms/EnviromentRegister'
import { SubjectRegister } from '../pages/forms/SubjectRegister'
import { Booking } from '../pages/forms/Booking'

export function PageRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Login />} />
                <Route path='initial' element={<Initial />}>
                    <Route index element={<Booking />} />
                    <Route path='subject' element={<SubjectRegister />} />
                    <Route path='teacher' element={<TeacherRegister />} />
                    <Route path='enviroment' element={<EnviromentRegister />} />

                </Route>
            </Routes>
        </BrowserRouter>
    )
}