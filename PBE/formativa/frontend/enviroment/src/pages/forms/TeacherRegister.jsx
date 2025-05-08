// import styles from './TeacherLogin.module.css'
import styles from './principal.module.css'
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { Navigate, useNavigate } from 'react-router';
import { useState } from 'react';

const loginSchema = z.object({
    nif: z.string().length(7, { message: 'Insert a valid ni (length:7)' }),
    subject: z.string().min(0, { message: 'Insert a valid subject' }),
    password: z.string().min(1, { message: 'Password can not be blank' }),
    username: z.string().min(3, { message: 'Insert a valid username' }),
    email: z.string().email({ message: 'Insert a valid email' }),
    phone: z.string().regex(/^\(\d{2}\) \d{5}-\d{4}$/, { message: 'Insert a valid cellphone (XX) XXXXX-XXXX' }),
    birth_date: z.string().refine((val) => /^\d{4}-\d{2}-\d{2}$/.test(val), {
        message: 'Birth date must be in YYYY-MM-DD format'
    }),
    hire_date: z.string().refine((val) => /^\d{4}-\d{2}-\d{2}$/.test(val), {
        message: 'Hiring date must be in YYYY-MM-DD format'
    }),
});

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
    const [profilePicture, setProfilePicture] = useState(null);

    const navegation = useNavigate()
    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: zodResolver(loginSchema)
    })

    function handleFormChange(e) {
        const { name, type, files, value } = e.target;
        const newValue = type === 'file' ? files[0] : value;
        setTeacherFormData(prev => ({ ...prev, [name]: newValue }));
        console.log(e.target.value);

    }


    async function userAutenticate(data) {
        const formData = new FormData();
        for (const [key, value] of Object.entries(data)) {
            formData.append(key, value);
        }

        if (profilePicture) {
            formData.append('profile_picture', profilePicture);
        }

        try {
            const response = await fetch('http://localhost:8000/api/accounts/', {
                method: 'POST',
                body: formData,
                headers: {'Content-Type': 'application/json'}
            });
            console.log(response);
            console.log(await response.json());
            
        } catch (error) {
            console.log(error);
        }
    }

    return (
        <div className={styles.container}>
            <p className={styles.title}>Teacher Register</p>

            <form
                encType="multipart/form-data"
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
                {errors.nif && (<p>{errors.nif.message}</p>)}
                <input
                    {...register('subject')}
                    placeholder='Subject'
                    className={styles.field}
                    name='subject'
                />
                {errors.subject && (<p>{errors.subject.message}</p>)}
                <input
                    {...register('password')}
                    placeholder='Password'
                    className={styles.field}
                    name='password'
                />
                {errors.password && (<p>{errors.password.message}</p>)}
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
                {errors.phone && (<p>{errors.phone.message}</p>)}
                <input
                    {...register('birth_date')}
                    type="date"
                    className={styles.field}
                />
                {errors.birth_date && (<p>{errors.birth_date.message}</p>)}
                <input
                    {...register('hire_date')}
                    type="date"
                    className={styles.field}
                />
                {errors.hire_date && (<p>{errors.hire_date.message}</p>)}
                <input
                    type="file"
                    className={styles.field}
                    onChange={(e) => setProfilePicture(e.target.files[0])}
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