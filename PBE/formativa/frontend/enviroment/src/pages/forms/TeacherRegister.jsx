import styles from './TeacherLogin.module.css'
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { Navigate, useNavigate } from 'react-router';
import { useState } from 'react';

const loginSchema = z.object({
    nif: z.string().length(7, { message: 'Insert a valid ni (length:7)' }),
    subject: z.string().min(1, { message: 'Insert a valid subject' }),
    username: z.string().min(3, { message: 'Insert a valid username' }),
    email: z.string().email({ message: 'Insert a valid email' }),
    phone: z.string().regex(/^\(\d{2}\) \d{5}-\d{4}$/, { message: 'Insert a valid cellphone (XX) XXXXX-XXXX' }),
    birthDate: z.string().transform((value) => new Date(value)),
    hiringDate: z.string().transform((value) => new Date(value))
})

export function TeacherRegister() {
    const [teacherFormData, setTeacherFormData] = useState({
        nif: '',
        username: '',
        password: '',
        subject: '',
        email: '',
        phone: '',
        birth_date: '',
        hire_date: '',
        profile_picture: ''
    })

    const navegation = useNavigate()
    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: zodResolver(loginSchema)
    })

    function handleFormChange(e) {
        setTeacherFormData({...teacherFormData, [e.target.name]: e.target.value})
        console.log(teacherFormData);

    }

    async function userAutenticate(data) {
        try {
            const response = await fetch('http://localhost:8000/api/accounts/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                body: JSON.stringify(teacherFormData)
            })
        } catch (error) {
            console.log(error);

        }
    }


    return (
        <div className={styles.container}>
            <p className={styles.title}>Teacher Register</p>

            <form
                onChange={handleFormChange}
                onSubmit={handleSubmit(userAutenticate)}
                className={styles.form}
            >
                <input
                    {...register('username')}
                    placeholder='Username'
                    className={styles.field}
                    name='username'
                />
                    {errors.username && (<p>{errors.username.message}</p>)}
                <input
                    {...register('nif')}
                    placeholder='NIF'
                    className={styles.field}
                    name='nif'
                />
                {errors.ni && (<p>{errors.ni.message}</p>)}
                <input
                    {...register('subject')}
                    placeholder='Subject'
                    className={styles.field}
                    name='subject'
                    />
                {errors.subject && (<p>{errors.subject.message}</p>)}
                <input
                    {...register('email')}
                    placeholder='E-mail'
                    className={styles.field}
                    name='email'
                />
                {errors.email && (<p>{errors.email.message}</p>)}
                <input
                    {...register('phone')}
                    placeholder='Cell phone'
                    className={styles.field}
                    name='phone'
                />
                {errors.cellphone && (<p>{errors.cellphone.message}</p>)}
                <input
                    {...register('birthDate')}
                    placeholder='Birth date'
                    className={styles.field}
                    type='date'
                    name='birth_date'

                />
                {errors.birthDate && (<p>{errors.birthDate.message}</p>)}
                <input
                    {...register('hiringDate')}
                    placeholder='Hiring date'
                    className={styles.field}
                    type='date'
                    name='hire_date'
                />
                {errors.hiringDate && (<p>{errors.hiringDate.message}</p>)}
                <input
                    {...register('profilePicture')}
                    placeholder='Profile Picture'
                    className={styles.field}
                    type='file'
                    name='profile_picture'
                />
                {errors.hiringDate && (<p>{errors.hiringDate.message}</p>)}
                <button
                    type='submit'
                    className={styles.button}
                >Login</button>
            </form>
        </div>
    );
}
